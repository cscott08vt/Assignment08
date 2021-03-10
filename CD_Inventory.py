#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# CScott, 2021-Mar-07, Added IO class, replaced pseudocode with actual code
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        ID: (int) with CD ID
        title: (string) with the title of the CD
        artist: (string) with the artist of the CD
    methods:
        __str__(): -> formatted string of CD objects
        file_str(): -> formatted string of CD objects
    """
    # -- Fields -- #
    # -- Constructor -- #
    
    def __init__(self, ID, title, artist):
        
        # -- Attributes -- #
        
        self.__ID = None
        self.__title = None
        self.__artist = None
        self.ID = ID
        self.title = title
        self.artist = artist

    # -- Properties -- #

    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, value):
        if type(value) == int:
            self.__ID = value
        else:
            raise Exception ('ID must be an integer')

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        self.__title = value

    @property
    def artist(self):
        return self.__artist

    @artist.setter
    def artist(self, value):
        self.__artist = value

    # -- Methods -- #

    def __str__(self):
        return '{}\t{}\t{}'.format(self.ID, self.title, self.artist)
    
    def file_str(self):
        return '{},{},{}\n'.format(self.ID, self.title, self.artist)
    
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, table): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    # -- Fields -- #
    # -- Constructor -- #
    # -- Properties -- #
    # -- Methods -- #
    @staticmethod
    def save_inventory(file_name, table):
        """Function to manage exporting data from list of lists to a file

        Writes the data to file identified by file_name from a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file that the data is written to
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        with open(file_name, 'w') as objFile:
            for line in table:
                objFile.write(line.file_str())
    
    @staticmethod
    def load_inventory(file_name, table):
        """Function to manage data ingestion from serialized file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of lists) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of lists): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        try:
            table.clear()  # this clears existing data and allows to load data from file
            with open(file_name, 'r') as objFile:
                for line in objFile:
                    data = line.strip().split(',')
                    cd = CD(int(data[0]),data[1],data[2])
                    table.append(cd)
        except FileNotFoundError as e:
            with open(file_name, 'w') as objFile:
               print('ERROR:'+ e.__doc__ +' An empty file called ' + file_name + ' was created within the working directory')
        except EOFError as e:
             print('The data file is empty! Current inventory is blank')

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Inputs and outputs data to/from user:

    properties:

    methods:
        print_menu(): -> None
        menu_choice(): -> (string) User choice
        show_inventory(table): -> None
        ID_title_artist_add(): -> intID, strTitle, strArtist

    """
    # -- Fields -- #
    # -- Constructor -- #
    # -- Properties -- #
    # -- Methods -- #
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
            """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')
    
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """
        Displays current inventory table

        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print(row)
        print('======================================')
        print() # Add extra space for layout

    @staticmethod
    def ID_title_artist_add():
        """Gets user input for specific CD to add

        Args:
            None.

        Returns:
            CD_info (list): list containing CD ID, title and artist

        """
        while True:
            try:
                intID = int(input('Enter ID: ').strip())
                break
            except ValueError as e:
                print('ERROR: ID that was entered is not of type: integer')
                print(e.__doc__)
                
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        print() # Add extra space for layout
        return intID, strTitle, strArtist

# 1. When program starts, read in the currently saved Inventory
FileIO.load_inventory(strFileName, lstOfCDObjects)
IO.show_inventory(lstOfCDObjects)

# 2. Start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()
    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName, lstOfCDObjects)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        intID, strTitle, strArtist = IO.ID_title_artist_add()
        CDObj = CD(intID, strTitle, strArtist)
        # 3.3.2 Add item to the table
        lstOfCDObjects.append(CDObj)
        # 3.3.3 Display current inventory after adding CD
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top
    # 3.5 process save inventory to file
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.6 catch-all should not be possible, as user choice gets vetted in IO, but to be safe:
    else:
        print('General Error')