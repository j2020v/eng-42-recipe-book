# Give it the necessary attributes
# Start defining methods


# all() --- have this on the db_class
    # gets all the instances from DB
        #get each record
        #create individual instances of recipe
        #store them in a list
        #return_list

def open_read_file_using_with(file):
    try:
        with open(file, 'r') as open_file:  # does not need to close method
            for line in open_file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError as errmsg:
        print('There has been a syntax error', errmsg)
        raise
    finally:
        print('\n Execution_completed')