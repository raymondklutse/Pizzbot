<!------------Intents---------------->
## intent:welcome_greet
- just going to say hi
- heya
- hello hi
- Heya
- howdy
- Howdy
- hey there
- hi there
- Hi
- hi
- Hi there
- greetings
- hey
- Hey
- long time no see
- hello

## intent:init_request
- I want pizza
- I want to order a pizza
- I want to order large pizza with olives
- I want lrge tomatoes pizza
- I want a medium cheese pizza

- I wnt to ordr a pijja
- I wntt piza

- wnt to oder pija
- wnt to oder lrg chezze piza
- wnt to odr mdim tamatas pija
- wnt to ordr least carn pijja
- wont laarg peper pijaa
- wnt mdm onins piza

- want to oder pija
- want to oder lrg chezze piza
- want to odr mdim tamatas pija
- want to ordr least carn pijja
- want laarg peper pijaa
- wnt mdm onins piza

- pizza
- pizza please
- Pizza please
- Pizza will do
- pizza will do
- Pizza
- pijja
- pija
- pijaa

- I like small olvs pizza
- pepperoni smll pizza
- larg onions

- My favorite pizza is Small corn
- my favorite pizza is small corn

- chese and SMALL
- mdm and Olives
- peperoni, lrg
- mall pizza with tmts topping
- medum with onion
- LARGE corns


## intent:init_pizza_question
- do you have pizza with no [meat](toppings)?
- do you have pizza with no [cheese](toppings)?
- do you have pizza with no [pepper](toppings)?
- do you have pizza with no [vegetables](toppings)?

- do you have pizza without [meat](toppings)?
- do you have pizza without [cheese](toppings)?
- do you have pizza without [pepper](toppings)?
- do you have pizza without [vegetables](toppings)?

- do you have pizza with no [meat](toppings) please?
- do you have pizza with no [cheese](toppings) please?
- do you have pizza with no [pepper](toppings) please?
- do you have pizza with no [vegetables](toppings) please?

- do you have pizza without [meat](toppings) please?
- do you have pizza without [cheese](toppings) please?
- do you have pizza without [pepper](toppings) please?
- do you have pizza without [vegetables](toppings) please?

- pizza with no [meat](toppings)?
- pizza with no [cheese](toppings)?
- pizza with no [pepper](toppings)?
- pizza with no [vegetables](toppings)?

- pizza without [meat](toppings)?
- pizza without [cheese](toppings)?
- pizza without [pepper](toppings)?
- pizza without [vegetables](toppings)?

- pizza with no [meat](toppings) please?
- pizza with no [cheese](toppings) please?
- pizza with no [pepper](toppings) please?
- pizza with no [vegetables](toppings) please?

- pizza without [meat](toppings) please?
- pizza without [cheese](toppings) please?
- pizza without [pepper](toppings) please?
- pizza without [vegetables](toppings) please?

- any pizza with no [meat](toppings)?
- any pizza with no [cheese](toppings)?
- any pizza with no [pepper](toppings)?
- any pizza with no [vegetables](toppings)?

- any pizza without [meat](toppings) please?
- any pizza without [cheese](toppings) please?
- any pizza without [pepper](toppings) please?
- any pizza without [vegetables](toppings) please?
 

## intent:item_start_generic
<!------------Examples
Two small fungi pizza
5 fungi pizza small
fungi pizza small 5
	---------------->
- I want [two](pizza_amount) [small](pizza_size) [Funghi](pizza_type) pizza 
- I want [one](pizza_amount) [Funghi](pizza_type) [small](pizza_size) pizza 
- I want [Funghi](pizza_type) pizza 
- I want [Funghi](pizza_type) pizza please
- I [hawaii](pizza_type) pizza small

- I want [Funghi](pizza_type) [small](pizza_size) pizza [three](pizza_amount)
- I want [four](pizza_amount) [small](pizza_size) pizza [Funghi](pizza_type)  
- I want [2](pizza_amount) [medium](pizza_size) pizza [hawaii](pizza_type) please

- [two](pizza_amount) [small](pizza_size) [Funghi](pizza_type) pizza 
- [two](pizza_amount) [medium](pizza_size) [Margherita](pizza_type) pizza 
- [2](pizza_amount) [large](pizza_size) [Hawaii](pizza_type) pizza 
- [two](pizza_amount) [medium](pizza_size) [Pepperoni](pizza_type) pizza 
- [4](pizza_amount) [small](pizza_size) [Vegetarian](pizza_type) pizza pizza 

- [four](pizza_amount) [small](pizza_size) pizza [Funghi](pizza_type) 
- [two](pizza_amount) [large](pizza_size) pizza [hawaii](pizza_type) 
- [four](pizza_amount) [medium](pizza_size) pizza [Margherita](pizza_type) 
- [4](pizza_amount) [large](pizza_size) pizza [Hawaii](pizza_type) 
- [four](pizza_amount) [medium](pizza_size) pizza [Pepperoni](pizza_type) 
- [four](pizza_amount) [small](pizza_size) pizza [Vegetarian](pizza_type) 

- [one](pizza_amount) [Funghi](pizza_type) [small](pizza_size) pizza 
- [one](pizza_amount) [Margherita](pizza_type) [medium](pizza_size) pizza 
- [1](pizza_amount) [Hawaii](pizza_type) [large](pizza_size) pizza 
- [one](pizza_amount) [Pepperoni](pizza_type)[medium](pizza_size) pizza  
- [3](pizza_amount) [Vegetarian](pizza_type) [small](pizza_size) pizza 

- [one](pizza_amount) [Funghi](pizza_type) pizza [small](pizza_size)  
- [one](pizza_amount) [Margherita](pizza_type) pizza [medium](pizza_size)  
- [1](pizza_amount) [Hawaii](pizza_type) pizza [large](pizza_size)  
- [one](pizza_amount) [Pepperoni](pizza_type) pizza[medium](pizza_size)   
- [3](pizza_amount) [Vegetarian](pizza_type) pizza [small](pizza_size)  

- [Funghi](pizza_type) [small](pizza_size) pizza [three](pizza_amount) 
- [Margherita](pizza_type) [medium](pizza_size) pizza [6](pizza_amount) 
- [Hawaii](pizza_type) [large](pizza_size) pizza [9](pizza_amount) 
- [Pepperoni](pizza_type)[medium](pizza_size) pizza  [4](pizza_amount) 
- [Vegetarian](pizza_type) [small](pizza_size) pizza [two](pizza_amount) 

- [Funghi](pizza_type) pizza [small](pizza_size)  [three](pizza_amount) 
- [Margherita](pizza_type) pizza [medium](pizza_size)  [6](pizza_amount) 
- [Hawaii](pizza_type) pizza [large](pizza_size)  [9](pizza_amount) 
- [Pepperoni](pizza_type) pizza [medium](pizza_size)   [4](pizza_amount) 
- [Vegetarian](pizza_type) pizza[small](pizza_size)  [two](pizza_amount) 

- [Funghi](pizza_type) pizza 
- [Margherita](pizza_type) pizza 
- [Hawaii](pizza_type) pizza 
- [Pepperoni](pizza_type) pizza 
- [Vegetarian](pizza_type) pizza pizza 

- [Funghi](pizza_type) 
- [Margherita](pizza_type) 
- [Hawaii](pizza_type) 
- [Pepperoni](pizza_type)
- [Vegetarian](pizza_type)

- [hawaii](pizza_type) pizza small
- [hawaii](pizza_type) pizza small please
- small [hawaii](pizza_type) pizza

- [two](pizza_amount) [medium](pizza_size) pizza [marherita](pizza_type) please

- [jumbo](pizza_type)

- [two](pizza_amount)
- [2](pizza_amount)

- [two](pizza_amount) please
- [2](pizza_amount) please
- [large](pizza_size) please
- [large](pizza_size)

- just [one](pizza_amount)
- just [1](pizza_amount)


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
- I want [funghi](pizza_type)
- I want [funghi](pizza_type) instead
- I want to change the size to [medium](pizza_size)
- I want to change the size to [large](pizza_size)
- I want my pizza in [small](pizza_size) instead

## intent:response_negative
- actually no
- nope
- no
- Nope
- No, I want to make a change

## intent:response_positive
- all good
- yep
- yeah
- perfect
- yes, that is right
- yes
- that's right
- correct
- Yes
- Yeah



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
- house number 46 street 655 avenue du technopole
- house num 46  655 avenue du technopole street
- Hs No 46  655 avenue du technopole street
- Hs No. 46  655 avenue du technopole street
- my address is house number 46 street 655 avenue du technopole
- my address is house num 46  655 avenue du technopole street
- my address is Hs No 46  655 avenue du technopole street
- my address is Hs No. 46  655 avenue du technopole street



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
- Small
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
