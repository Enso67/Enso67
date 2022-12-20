#1. Read the data from the Streaming_Services.txt file provided in the assignment.

filename = "Streaming_Services.txt"
file_mode = "r"
output_file = open(filename, file_mode)
contents = output_file.readlines()

#print(contents)

#2. Store the data in an appropriate container.
stream_prices = []
#3. Output the average price of all services.
for i in contents[1:]:
    line = (i.split())
    price = float(line[1])
    stream_prices.append(price)
print(stream_prices)

average_stream = (sum(stream_prices))/ len(stream_prices)
#print("The average price is " "%.2f" % average_stream)
#4. Write the average price to a new file called [Name]_Files_Lab.txt. Replace [Name] with your name.
#file = open("[Kyle_Metcalf]_Files_Lab.txt", "a")
#file.write("The average price is " "%.2f" % average_stream)
#file.close
#5. Upload your script and output file to Moodle.
file = open("[Kyle_Metcalf]_Files_Lab.txt", "r")
print(file.read())
