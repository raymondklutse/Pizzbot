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
- Large
- size L

## synonym:18"
- 18
- jumbo
- XXL
- size XXL

<!---Pizza Type-->
## synonym:Funghi
- Funghi
- funghi

## synonym:Hawaii
- Hawaii
- hawaii

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
- vegetarian

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
- yeah i am confirming it here
- yep
- yes
- that's right
- correct

## intent:init_request
- I want pizza
- I want to order a pizza
- pizza
- Pizza please
- Pizza will do
- Pizza
- pijja
- pija
- pijaa
- wnt to oder pija
- I wnt to ordr a pijja
- I wntt piza
- I want to order large pizza with olives
- I like small olvs pizza
- pepperoni smll pizza
- larg onions
- I want lrge tomatoes pizza
- My favorite pizza is Small corn
- I want a medium cheese pizza
- chese and SMALL
- mdm and Olives
- peperoni, lrg
- mall pizza with tmts topping
- medum with onion
- LARGE corns
- wnt to oder lrg chezze piza
- wnt to odr mdim tamatas pija
- wnt to ordr least carn pijja
- wont laarg peper pijaa
- wnt mdm onins piza

## intent:item_start_generic
- [two](pizza_amount) [medium](pizza_size) pizza [marherita](pizza_type) please
- [jumbo](pizza_type)
- [hawaii](pizza_type) pizza [two](pizza_amount) please
- i want to order [2](pizza_amount) pizza.
- can i have [large](pizza_size) pizza please
- I want [2](pizza_amount) [medium](pizza_size) pizza [hawaii](pizza_type) please
- [one](pizza_amount) pizza [funghi](pizza_type)
- i'd like [three](pizza_amount) [medium](pizza_size) pizza [margherita](pizza_type)
- I'd like to order [3](pizza_amount)  [small](pizza_size) [hawaii](pizza_type) please

## intent:item_change
- I changed my mind. Can I get  a [funghi](pizza_type) instead?
- I'd like a  [margherita](pizza_type) pizza instead.
- can i get a [vegetarian](pizza_type) instead?
- actually , can I get [margherita](pizza_type)?
- actually , i 'd like [small](pizza_size) pizza.
- I'd like in [small](pizza_size) instead.
- actually, i would like a [small](pizza_size) [vegetarian](pizza_type).
- wait, can i get  it in [large](pizza_size).
- i want [large](pizza_size).

## intent:item_change_request_without_entity
- Actually i want to modify pizza type.
- Actually i want to modify pizza size.
- i want to change my order.

## intent:item_type_start_negative
- do you have [Americana](pizza_type)
- do you offer pizza [Americana](pizza_type)

## intent:item_type_start_positive
- do you have [hawaii](pizza_type)
- do you offer pizza [margherita](pizza_type)

## intent:item_type
- [hawaii](pizza_type)
- [margherita](pizza_type)

## intent:item_size
- [small](pizza_size)
- [large](pizza_size)
- I want to order Large pizza
- I want a Laarg pizza
- I think its laarge
- medim pija
- huge pijja
- Little piza
- Probably avg
- smll
- lrg
- midum
- large

## intent:item_topping

- I want to order pizza with OLIVES
- My favourite topping is cheze
- I like olive
- Pepperoni is my favorite topping
- Definitely onnion
- I love tomotos
- favorite topping is Corns
- I love cheeze
- chesse
- Oliv
- Peperroni
- tomotoes
- Onions
- Corn


## intent:item_amount
- [3](pizza_amount)
- [2](pizza_amount)

## intent:pizza_questions
- do you have [hawaii](pizza_type)
- do you offer pizza [margherita](pizza_type)


## intent:order_take_home
- take away
- i prefer take away
- take away please

## intent:order_delivery
- delivery please
- delivery
- i prefer delivery

## intent:order_delivery_address
- my address is #46, 655 avenue du technopole
- #46, 655 avenue du technopole

## intent:order_confirm_final
- i am done
- actually i dont want anything else
- no i am done now.
- no i am done.
- nope
- no.

