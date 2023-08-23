def write_file(file_name, file_content):
    
        with open(file_name, mode='w') as file:
            file.txl.write(file_content)
        print("File written successfully.")
  

def append_file(file_name, append_content):
    
        with open(file_name, mode='a') as file:
            file.write(append_content)
        print("Content appended successfully.")
   

def read_file(file_name):
    
        with open(file_name, mode='r') as file:
            content = file.read()
            return content
   
                 