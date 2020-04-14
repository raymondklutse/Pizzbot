# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class PizzaOrderForm(FormAction):

	def name(self) -> Text:
		"""Unique identifier of the form"""
		return "pizza_order_form"

	@staticmethod
	def required_slots(tracker: Tracker) -> List[Text]:
		"""A list of required slots that the form has to fill"""
		return ["pizza_type", "pizza_amount","pizza_size"]

	def submit(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict]:
		"""Define what the form has to do after all required slots are filled"""
		pizza_size = tracker.get_slot("pizza_size")
		pizza_type = tracker.get_slot("pizza_type")
		pizza_amount = tracker.get_slot("pizza_amount")
		
		dispatcher.utter_message(text='Okay Great. Your order is {} {} pizzas in {}. Can you confirm please'.format(pizza_amount,pizza_type,pizza_size))
		return []


class ChangeOrderAction(Action):

	def name(self):
		return 'action_change_order'

	def run(self, dispatcher, tracker, domain):
		Slot_to_be_reset_name = tracker.get_slot("pizza_type")
		pizza_size = tracker.get_slot("pizza_size")
		pizza_type = tracker.get_slot("pizza_type")
		pizza_amount = tracker.get_slot("pizza_amount")
		SlotSet("pizza_type", pizza_type)
		SlotSet("pizza_size", pizza_size)
		SlotSet("pizza_amount", pizza_amount)
		return[]

    