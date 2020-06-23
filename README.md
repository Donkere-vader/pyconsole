# Console
A simple module to make your program's outpur a lot better
(for python)

## Console class
### defining the console
```
console = Console(program_name='NameOfProgram', log=True, pin=None, log_display_length=10)
```
#### Parameters
**program_name**: str  
The name of your program

**log**: bool  
If set to true there will be a log file in the folder ./logs

**pin**  
you can provide an object here that will always be displayed above the logs. This could for example be a table (which is also included in the module) with the program data such as online users or progress for example.

**log_display_length**: int  
The maximum amount of log items to be displayed in the terminal. (This has no effect on the log file)

### Outputting to the console
To output to the console simply do;
```
console.log('some string')
```
The console class will automatically timestamp it


### Table class
defining the table
```
table = Table(self, values: list, column_names=[], row_names=[], borders=None, max_column_width=100, max_row_height=100)
```
**values**: list  
Provide an list in a list list.  
example:
```
[
    [
        "row1 item1", "row1 item2"
    ],
    [
        "row2 item1", "row2 item2"
    ]
]
```

**column_names**: list  
Provide a list of str for the column names to be displayed above the columns

**row_names**: list  
Provide a list of str for the row names to be displayed left of the rows

**border**: str  
Doesn't do anything. (yet?)

**max_column_width**: int  
The maximum width a column can have

**max_row_height**: int  
The maximum height a row can have. Although a row can't be higher than one line for now.