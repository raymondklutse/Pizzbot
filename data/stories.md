##greeting
* welcome_greet
  - utter_welcome_greet
> start_questions_on_pizza
> start_order

## questions_on_pizza
> start_questions_on_pizza
* init_pizza_question
  - utter_init_pizza_question
> start_order

## order pizza vague
> start_order
* init_request
  - utter_init_request
* item_start_generic
  - pizza_order_form
  - form{"name": "pizza_order_form"}
> confirm_order
> confirm_order_pre_question

## order pizza precise
> start_order
> new_order
* item_start_generic
  - pizza_order_form
  - form{"name": "pizza_order_form"}
> confirm_order
> confirm_order_pre_question

## story_to_modify_order
> confirm_order
* response_negative
  - action_change_order
  - utter_item_change
> confirm_order

## story_to_modify_order_2
> confirm_order
* item_change
  - action_change_order
  - utter_item_change
> confirm_order

## story_to_modify_order_3
> confirm_order
* response_negative
  - utter_order_confirm_negative
* item_change
  - action_change_order
  - utter_item_change
> confirm_order

## story_to_proceed_furthur
> confirm_order
* response_positive
  - action_pizza_order_add
  - utter_extra_order
> confirmed_order_proceed 

## story_to_add_new_order
> confirmed_order_proceed
* response_positive
  - action_reset_pizza_form
  - utter_order_add
> new_order

## story_to_proceed_with_confirm_order
> confirmed_order_proceed
* response_negative
  - utter_total_order_final
> order_proceed

## order take home
> order_proceed
* order_take_home
  - utter_order_complete

## order delivery
> order_proceed
* order_delivery
  - utter_delivery_address
* order_delivery_address
  - utter_order_complete

## story_modify_prerequest
> confirm_order_pre_question
* item_change_request_without_entity
  - utter_item_type
> confirm_order

