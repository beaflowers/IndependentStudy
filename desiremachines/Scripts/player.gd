# Attach this script to a CharacterBody2D node.
extends CharacterBody2D

# Exported variable allows you to change the speed directly in the Inspector.
@export var speed = 200.0

var left_random_multiplier = 1.0
var right_random_multiplier = 1.0

func _ready():
	print("Script running!")
	_update_random()
	
func _update_random():
	#introduce randomness into player movement
	left_random_multiplier = randf_range(-2, 10)
	right_random_multiplier = randf_range(-2, 10) 
	print("Random Multipliers - Left: ", left_random_multiplier, " Right: ", right_random_multiplier)
	
func get_input():
	#left player movement
	var leftPlayer = Input.get_vector("leftplayer_left", "leftplayer_right", "leftplayer_up", "leftplayer_down")
	#right player movement
	var rightPlayer = Input.get_vector("rightplayer_left", "rightplayer_right", "rightplayer_up", "rightplayer_down")
	
	#multiples by random number generator to create chaos
	leftPlayer = leftPlayer * left_random_multiplier
	rightPlayer = rightPlayer * right_random_multiplier
	
	#average for direction
	var direction = (leftPlayer + rightPlayer) / 2
	
	velocity = direction * speed
		
	
func _physics_process(delta: float) -> void:
	get_input()
	move_and_slide()

func _on_timer_timeout() -> void:
	#timer length is set in Node rather than in code
	_update_random() 
