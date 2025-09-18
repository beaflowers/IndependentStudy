# Attach this script to a CharacterBody2D node.
extends CharacterBody2D

# Exported variable allows you to change the speed directly in the Inspector.
@export var speed = 200.0

func _ready():
	print("Script running!")
	
func get_input():
	#left player movement
	var leftPlayer = Input.get_vector("leftplayer_left", "leftplayer_right", "leftplayer_up", "leftplayer_down")
	
	#right player movement
	var rightPlayer = Input.get_vector("rightplayer_left", "rightplayer_right", "rightplayer_up", "rightplayer_down")
	
	#average for direction
	
	var direction = (leftPlayer + rightPlayer) / 2
	
	velocity = direction * speed
		
	
func _physics_process(delta: float) -> void:
	get_input()
	move_and_slide()
