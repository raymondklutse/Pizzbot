<!---Lookup-->
## lookup:anti_pizza_type
data/lookup_tables/anti_pizza_type.txt

## lookup:pizza_size
data/lookup_tables/pizza_size.txt

## lookup:pizza_type
data/lookup_tables/pizza_type.txt

## lookup:pizza_amount
data/lookup_tables/pizza_amount.txt

<!-----------Synonyms--------------->
<!---Pizza Anti Type-->
## synonym:Americana
- Americana

## synonym:Calzone
- Calzone

## synonym:Caprese
- Caprese

## synonym:Crudo
- Crudo

## synonym:Chicken BBC
- Chicken BBC

## synonym:Rustica
- Rustica

<!---Pizza Size-->
## synonym:10"
- 10
- 10 inch
- small
- size S

## synonym:12"
- 12
- 12 inch
- Medium
- medium
- normal
- twelve inch
- size M

## synonym:14"
- 14
- 14 inch
- large
- size L

## synonym:18"
- 18
- jumbo
- XXL
- size XXL

<!---Pizza Type-->
## synonym:Funghi
- Funghi

## synonym:Hawaii
- Hawaii

## synonym:Margherita
- Margherita
- margherita

## synonym:Pepperoni
- Pepp

## synonym:Vegetarian
- Vegetarian
- Vegetaria
- Vegetable
- Vegetarian

<!------------Intents---------------->
## intent:welcome_greet
- just going to say hi
- heya
- hello hi
- howdy
- hey there
- hi there
- greetings
- hey
- long time no see
- hello

## intent:item_confirm_no
- i am not done yet
- actually no
- nope
- no

## intent:item_confirm_yes
- all good
- yeah
- yep
- yes
- that's right
- correct

## intent:item_size_change
- actually , i 'd like [small](pizza_size) pizza
- I'd like in [small](pizza_size) instead
- actually, i would like a [small](pizza_size) [vegetarian](pizza_type).
- wait, can i get  it in [large](pizza_size)


## intent: item_start_generic
- [two](pizza_amount) [large](pizza_size) pizza [marherita](pizza_type) please
- [jumbo](pizza_type)
- [two](pizza_amount) please
- [2](pizza_amount)
- [large](pizza_size) please
- just [one](pizza_amount)
- order please
- [one](pizza_amount) pizza [funghi](pizza_type)
- i'd like [three](pizza_amount) [large](pizza_size) pizza [margherita](pizza_type)
- I'd like to order [3](pizza_amount)  [large](pizza_size) [hawaii](pizza_type) please

## intent:item_type_change
- I changed my mind. Can I get  a [funghi](pizza_type) instead?
- I'd like a  [margherita](pizza_type) pizza instead.
- can i get a [vegetarian](pizza_type) instead?
- actually , can I get [margherita](pizza_type)?

## intent:item_type_start_negative
- do you have [Americana](pizza_type)
- do you offer pizza [Americana](pizza_type)

## intent:item_type_start_positive
- do you have [hawaii](pizza_type)
- do you offer pizza [margherita](pizza_type)

## intent:item_type
- hawaii](pizza_type)
- [margherita](pizza_type)

## intent:item_size
- [small](pizza_size)
- [large](pizza_size)

## intent:item_amount
- [3](pizza_amount)
- [2](pizza_amount)

## intent:pizza_questions
- do you have [hawaii](pizza_type)
- do you offer pizza [margherita](pizza_type)
