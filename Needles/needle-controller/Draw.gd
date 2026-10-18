extends Node2D

@onready var _lines: Node2D = $Line2D

const GRAVITY = 1500.0
const FALL_LENGTH = 300.0 #pieces shorter than this will fall

var ERASE_RADIUS = 16
var _erase_origin: Vector2
var _erase_armed: bool = false
var _erase: bool = false
var _current_line: Line2D = null
var _falling: Array[Line2D] = []

func _ready() -> void:
	_new_line()
	
func _piece_length(pts: PackedVector2Array) -> float:
	var total := 0.0
	for i in range(pts.size() - 1):
		total += pts[i].distance_to(pts[i+1])
	return total

func _new_line() -> void:	
	_current_line = Line2D.new()
	_current_line.width = 24

	#gradient color
	var gradient := Gradient.new()
	gradient.set_color(0, Color.FUCHSIA)
	gradient.set_color(1, Color.DEEP_SKY_BLUE)
	gradient.add_point(0.25, Color.MEDIUM_PURPLE)
	gradient.add_point(0.75, Color.PALE_GREEN)
	_current_line.gradient = gradient

	_lines.add_child(_current_line)
	_current_line.begin_cap_mode = Line2D.LINE_CAP_ROUND
	_current_line.end_cap_mode = Line2D.LINE_CAP_ROUND
	_current_line.joint_mode = Line2D.LINE_JOINT_ROUND
	_current_line.add_point(get_local_mouse_position())
	
func _erase_at(pos: Vector2) -> void:	
	for line: Line2D in _lines.get_children():
		if line.is_queued_for_deletion() or line.has_meta("velocity"):
			continue
		
		var pts := line.points
		if pts.size() < 2:
			continue
			
		var pieces: Array[PackedVector2Array] = []
		var run := PackedVector2Array()
		var hit := false
		
		for i in range(pts.size() - 1):
			var closest := Geometry2D.get_closest_point_to_segment(pos, pts[i], pts[i+1])
			if closest.distance_to(pos) < ERASE_RADIUS:
				hit = true
				if run.size() >= 2:
					pieces.append(run)
				run = PackedVector2Array()	
			else: 
				if run.is_empty():
					run.append(pts[i])
				run.append(pts[i+1])
				
		if not hit:
			continue
			
		if run.size() >= 2:
			pieces.append(run)
			
		for piece in pieces:
			var new_line := Line2D.new()
			new_line.width = line.width
			new_line.gradient = line.gradient
			new_line.begin_cap_mode = Line2D.LINE_CAP_ROUND
			new_line.end_cap_mode = Line2D.LINE_CAP_ROUND
			new_line.joint_mode = Line2D.LINE_JOINT_ROUND
			new_line.points = piece
			_lines.add_child(new_line)
			
			if _piece_length(piece) < FALL_LENGTH:
				new_line.set_meta("velocity", Vector2.ZERO)
				_falling.append(new_line)
			
		line.queue_free()
				
func _input(event: InputEvent) -> void:
	if event is InputEventMouseButton and event.pressed and event.button_index == MOUSE_BUTTON_LEFT:
		_erase = not _erase
		if _erase:
				_erase_origin = event.position
				_erase_armed = false
		else:
			_new_line()
			
	if event is InputEventMouseMotion:
		if _erase:
			if not _erase_armed and event.position.distance_to(_erase_origin) > ERASE_RADIUS * 2.0:
				_erase_armed = true          # erase turns on when double size of erase radius away from click position
			if _erase_armed:
				_erase_at(event.position)
		else:
			_current_line.add_point(event.position)

func _lowest_y(line: Line2D) -> float:
	var lowest := -INF
	for p in line.points:
		lowest = maxf(lowest, p.y)
	return lowest
		
func _process(delta: float) -> void:
	var floor_y := get_viewport_rect().size.y
	
	for line: Line2D in _falling.duplicate():
		if not is_instance_valid(line):
			_falling.erase(line)
			continue
		
		var vel: Vector2 = line.get_meta("velocity")
		vel.y += GRAVITY * delta
		line.set_meta("velocity", vel)
		line.position += vel * delta
		
		var bottom := _lowest_y(line) + line.position.y + line.width / 2.0
		if bottom >= floor_y:
			_land(line, bottom - floor_y)
				
func _land(line: Line2D, overshoot: float) -> void:
	line.position.y -= overshoot
	
	var pts := line.points
	for i in pts.size():
		pts[i]+= line.position
	line.points = pts
	line.position = Vector2.ZERO
	
	line.remove_meta("velocity")
	_falling.erase(line)
