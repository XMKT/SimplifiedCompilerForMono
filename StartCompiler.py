class CompilerCSharp:

    def File(name):
        if name.endswith('.cs'):
            FileName = str(name)
        else:
            FileName = str(name) + '.cs'
        return FileName

    def Compiler(FileName, t='dmcs'):
        BatFile = open('Compiler.bat', 'w')
        BatFile.write('python StartCompiler.py\n')
        BatFile.write(t + ' ' + FileName + '\n')

def main():
    print('выбирете файл для компиляции')
    print('для показа списка доступных команд напишите: cm')
    UserInput = str(input(''))
    CommandLIst = {
        'help': 'если вы хотите изменить режим компиляции, напишите в начале ее тип а потом название файла',
        'типы компиляции': '| mcs | gmcs | smcs | dmcs |',
    }
    HelpCommand = CommandLIst.get(UserInput)

    if HelpCommand == None:
    	words = UserInput.split(' ')

    	if len(words) == 2:
    		FileName = words[1]
    		type_compile = words[0]
    		Name = CompilerCSharp.File(FileName)
    		CompilerCSharp.Compiler(Name,type_compile)
    	elif len(words) == 1:
    		FileName = words[0]
    		Name = CompilerCSharp.File(FileName)
    		CompilerCSharp.Compiler(Name)

    	else:
    		print('<<Тип>>(необязательно) + <<Имя файла>>')

    elif HelpCommand == 'cm':
    	array = HelpCommand.keys()
    	for i in array:
    		print(i)

if __name__=='__main__':
	main()