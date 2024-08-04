**Phone Book**

#### Video Demo:  https://youtu.be/Pnxpt5aicrA

#### Description:

This program is a phone book where you can add a name and phone number to it by selecting the appropriate option. Search for a name and access its number or remove a contact from the 	list or see all contacts
To run this program, you must write an argument containing the name of a file with the extension .txt in the command line, for example:
python project.py file.txt

### **def validation:**
In the validation function, it checks whether the given file is correct or not

### **def main:**
In the main function of the menu, it will be shown to you that you can add a contact by entering the number 1. Search for a specific contact by entering the number 2. Delete a contact by 	entering the number 3. By entering the number 4, all contacts will be displayed and exit the program by entering the number 0.
### **def add:**
The add function takes a **name** and a **number**. In the PATH file, enter the address as:
 Writes **name:number** in the file

### **def search**
The search function takes a word named name and then checks whether the file exists or not using the validation function, and if   it does not exist, it creates the validation.
Then, by opening the file and using read mode, it reads the lines one by one and wherever it reaches the desired name, it prints that line.
### **def delete:**
In the delete function that takes an input as a name. After opening the PATH file, it reads its lines one by one. If it is reading a line that does not contain a name, it writes that line in a new variable. If the name is in the line it reads, it does not add it to the new variable. At the end, the function returns the new variable as output
