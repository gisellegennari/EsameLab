class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    def __init__(self, name):

        # Setto il nome del file
        self.name = name

    def get_data(self):
        # Inizializzo una lista vuota per salvare i valori
        values = []
        values2 = []  #lista che contiene giorno per giorno

        # Provo ad aprire il file per estrarci i dati. Se non ci riesco, prima avverto del'errore,
        # poi devo abortire. Questo e' un errore "un-recoverable", ovvero non posso proseguire con
        # la lettura dei dati se non riesco ad aprire il file!
        try:
            my_file = open(self.name, 'r')
        except Exception as e:

            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))

            # Esco dalla funzione tornando "niente".
            return None

        # Ora inizio a leggere il file linea per linea
        for line in my_file:

            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'epoch' and elements[1] != 'temperature':

                # Setto la data ed il valore
                #date  = elements[0]
                value = elements[0]
                value2 = elements[1]

                # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo,
                # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
                # un errore "recoverable", posso proseguire (semplicemente salto la linea).
                try:
                    value = int(value)
                    value2 = float(value2)
                except Exception as e:

                    # Stampo l'errore
                    print('Errore nela conversione a float: "{}"'.format(e))

                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue

                # Infine aggiungo alla lista dei valori questo valore
                values.append(value)
                values.append(value2)

                #inserisco i primi valori della lista nella lista
                values2.append(values)
                values = []

        # Chiudo il file
        my_file.close()

        # Quando ho processato tutte le righe, ritorno i valori
        return values2

    def daily_stats(self, time_series):
      ##day_start_epoch = 0
      #return time_series
      i = 0
      #############contaElementiLIST = []
      while i < len(time_series):
        ###day_start_epoch = time_series[i] - (time_series[i] % 86400)
        #return time_series[2]
        ##############contaElementiLIST = time_series[i]
        while j < len(time_series):

          j+=1
          
        i+=1

      #######return contaElementiLIST

#======================
# Corpo del programma
#======================

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
time_series2 = time_series_file.daily_stats(time_series)

#print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(time_series2))
