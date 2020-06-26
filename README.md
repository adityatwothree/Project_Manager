## Project Manager
- This app contains multiple boards to signify different projects
- Each board contains different lists to signify sub-project
- Each list contain different cards signifying smaller tasks
- Each card can be assigned to a user or may remain unassigned

## Input

- There will be different types of input:
    - BOARD CREATE <board_name>
    - BOARD <board_id> <name/privacy> <new_value> 
    - BOARD <board_id> <ADD_MEMBER/REMOVE_MEMBER> <user_id>
    - BOARD DELETE <board_id>
    - LIST CREATE <board_id> <list_name>
    - LIST <list_id> <name> <new_value>
    - LIST DELETE <list_id>
    - CARD CREATE <list_id> <card_name>
    - CARD <card_id> <name/description> <new_value> 
    - CARD <card_id> ASSIGN <user_id>
    - CARD <card_id> UNASSIGN
    - CARD <card_id> MOVE <target_list_id> 
    - CARD DELETE <card_id>
    - SHOW
    - SHOW BOARD <board_id>
    - SHOW LIST <list_id>
    - SHOW CARD <card_id>


## Output

- CREATE operations prints the id after creation
- SHOW will print all the boards with all the lists inside them and all the cards inside all the lists (including all the attributes)
- SHOW <BOARD/LIST> should print that specific entity and everything inside it (including all the attributes)
- SHOW CARD will print all the attributes of the card
-All the information is printed in JSON format
