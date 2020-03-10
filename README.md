# c-kvdily
პროგრამა არის C ენის ქვესიმრავლის კომპილატორი 32-ბიტიანი სისტემებისთვის.

პროგრამას შეუძლია შემდეგი შუამავალი ნაბიჯების დაბეჭდვა:
* საწყისი C კოდი
* Token-ებად დაშლილი კოდი (Lexing)
* Abstract Syntax Tree (AST)
* Assembly კოდი

მაგალითისთვის, ეს არის return_99.c კოდის კომპილაციისას გენერირებული output-ი:
```
Compiling return_99.c

Tokenized code:
<"int" | TYPE: INT>
<"main" | TYPE: IDENTIFIER>
<"(" | TYPE: OPEN_PARENTHESIS>
<")" | TYPE: CLOSE_PARENTHESIS>
<"{" | TYPE: OPEN_BRACE>
<"return" | TYPE: RETURN>
<"99" | TYPE: INTEGER_LITERAL>
<";" | TYPE: SEMICOLON>
<"}" | TYPE: CLOSE_BRACE>

Abstract Syntax Tree:
PROGRAM:
	FUNCTION int main:
		RETURN CONST 99

Assembly code:
	.globl main
main:
	movl $99, %eax
	ret

Creating executable file named return_99
Compiled successfully!
```
## გამოყენების ინსტრუქცია
თუ გვსურს example.c-ის კომპილაცია, ტერმინალში ჩავწერთ:
```
python3 compiler.py example.c
```
ან
```
./compiler.py example.c
```
გაითვალისწინეთ რომ *c-kvdily* იყენებს *gcc*-ს ასემბლერიდან ორობითი კოდის გენერაციისთვის.
## ტესტები
ჯერ-ჯერობით მუშაობს stage_1 და stage_2. ტესტების გასაშვებად აკრიფეთ:
```
./test_compiler.sh ./compiler.py 1 2
```
## ავტორები

ამ ეტაპზე კომპილატორი დაწერილია მხოლოდ ჩემს მიერ [ამ სტატიების](https://norasandler.com/2017/11/29/Write-a-Compiler.html) მიხედვით. 
სატესტო ფაილები მისი ავტორისგან მაქვს აღებული.
