import pandas as pd 

df = pd.read_csv('categories/cost-of-living-clean.csv')

food = df[['Meal, Inexpensive Restaurant','Meal for 2 People, Mid-range Restaurant, Three-course','McMeal at McDonalds (or Equivalent Combo Meal)','Coke/Pepsi (0.33 liter bottle)','Water (0.33 liter bottle) ','Milk (regular), (1 liter)','Loaf of Fresh White Bread (500g)','Eggs (regular) (12)','Local Cheese (1kg)','Water (1.5 liter bottle)','Chicken Breasts (Boneless, Skinless), (1kg)','Apples (1kg)','Oranges (1kg)','Potato (1kg)','Lettuce (1 head)','Cappuccino (regular)','Rice (white), (1kg)','Tomato (1kg)','Banana (1kg)','Onion (1kg)','Beef Round (1kg) (or Equivalent Back Leg Red Meat)','Country','Capital']]
transport = df[['One-way Ticket (Local Transport)','Monthly Pass (Regular Price)','Gasoline (1 liter)','Taxi Start (Normal Tariff)','Taxi 1km (Normal Tariff)','Taxi 1hour Waiting (Normal Tariff)','Volkswagen Golf','Toyota Corolla 1.6l 97kW Comfort (Or Equivalent New Car)','Country','Capital']]
apartment = df[['Apartment (1 bedroom) in City Centre','Apartment (1 bedroom) Outside of Centre','Apartment (3 bedrooms) in City Centre','Apartment (3 bedrooms) Outside of Centre','Country','Capital']]
expenses = df[['Basic (Electricity, Heating, Cooling, Water, Garbage) for 85m2 Apartment','Mortgage Interest Rate in Percentages (%), Yearly, for 20 Years Fixed-Rate','Country','Capital']]
school = df[['Preschool (or Kindergarten), Full Day, Private, Monthly for 1 Child','International Primary School, Yearly for 1 Child','Country','Capital']]
clothing = df[['1 Pair of Jeans (Levis 501 Or Similar)','1 Summer Dress in a Chain Store (Zara, H&M, ...)','1 Pair of Nike Running Shoes (Mid-Range)','1 Pair of Men Leather Business Shoes','Country','Capital']]
entertainment = df[['Domestic Beer (0.5 liter draught)','Imported Beer (0.33 liter draught)','Domestic Beer (0.5 liter bottle)','Imported Beer (0.33 liter bottle)','Cigarettes 20 Pack (Marlboro)','1 min. of Prepaid Mobile Tariff Local (No Discounts or Plans)','Internet (60 Mbps or More, Unlimited Data, Cable/ADSL)','Fitness Club, Monthly Fee for 1 Adult','Tennis Court Rent (1 Hour on Weekend)','Cinema, International Release, 1 Seat','Country','Capital']]
salary = df[['Average Monthly Net Salary (After Tax)','Country','Capital']]

food.to_csv('categories/food.csv')
transport.to_csv('categories/transport.csv')
apartment.to_csv('categories/apartment.csv')
expenses.to_csv('categories/expenses.csv')
school.to_csv('categories/school.csv')
clothing.to_csv('categories/clothing.csv')
entertainment.to_csv('categories/entertainment.csv')
salary.to_csv('categories/salary.csv')
