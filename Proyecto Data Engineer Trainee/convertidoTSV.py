import codecs


class Converter:
    
    def __init__(self,input_file) -> None:
        self.input_file = input_file
        self.row = str()
        self.total_rows = int()
        self.delimiter = str()
        
    def count_columns(self, file) -> None:
        '''
        cuenta el número de columnas de un archivo
        '''
        self.total_rows = len(file.readline().split('\t'))
        file.seek(0)
        
        
    def write_in_csv(self, line, file) -> None:
        '''
        Escribe una línea en el archivo de salida especificado.
        '''
        with open(file,'a') as files:
            line = self.clean_row(line)
            file.write(f'{line}')
            
            
    def clean_row(self,line) ->str:
        '''
        limpia la fila antes de insertarla en el archivo
        '''
        if not '\n' in line:
            last_line = True
        else:
            last_line = False
            
        rows = line.split(self.delimiter)
        final_line = str()
        for i in range(0,self.total_rows):
            if i == self.total_rows -1 and not last_line:
                final_line +=f'{rows[i].rstrip().lstrip()}\n'
            elif i == self.total_rows -1 and last_line:
                final_line += f'{rows[i].rstrip().lstrip()}'
            else:
                rows[i] = rows[i].replace('\n',' ')
                final_line += f'{rows[i].rstrip().lstrip()}{self.delimiter}'
                
        return final_line
    


    def convert_to_csv(self,output_file,delimiter) ->None:
        '''
        Función principal para leer el archivo de entrada y convertir sus datos en un archivo csv
        Parámetros: el nombre del archivo de salida csv y el delimitador de la salida csv
        '''
        self.delimiter = delimiter
        
        with codecs.open(self.input_file,'r', encoding='utf-16-le') as file:
            self.count_columns(file)
            for line in file:
                if len(line.rstrip().split('\t')) == self.total_rows:
                    line = self.clean_row(line.replace('\t',self.delimiter))
                    self.write_in_csv(line,output_file)
                else:
                    self.row +=line.replace('\t',self.delimiter)
                    
                    
                    
                if len(self.row.split(self.delimiter)) == self.total_rows:
                    self.row = self.clean_row(self.row)
                    self.write_in_csv(self.row, output_file)
                    self.row = str()
                    
        print('Archivo convertido exitosamente a CSV')
        
if __name__ == '__main__':
        Converter('datos_data_engineer.tsv').convert_to_csv('datos_data_engineer.csv',delimiter='|')