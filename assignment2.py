#createCollection(p_collection_name)
def getDepFacet(p_collection_name):
    if p_collection_name in collections:
        dep_count = {}
        for emp in collections[p_collection_name]:
            dept = emp.get('Department')
            if dept:
                if dept not in dep_count:
                    dep_count[dept] = 0
                dep_count[dept] += 1
        print("Employee count by department:", dep_count)
    else:
        print(f"Collection '{p_collection_name}' does not exist.")
        
#indexData(p_collection_name, p_exclude_column)

def indexData(p_collection_name, p_exclude_column, employee_data):
    if p_collection_name in collections:
        for employee in employee_data:
            if p_exclude_column in employee:
                del employee[p_exclude_column]
            collections[p_collection_name].append(employee)
        print(f"Data indexed into '{p_collection_name}', excluding column: {p_exclude_column}.")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")
        
#searchByColumn(p_collection_name, p_column_name, p_column_value)

def searchByColumn(p_collection_name, p_column_name, p_column_value):
    if p_collection_name in collections:
        results = [emp for emp in collections[p_collection_name] if emp.get(p_column_name) == p_column_value]
        print(f"Results for search on {p_column_name} = {p_column_value}: {results}")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")
        
#getEmpCount(p_collection_name)
def getEmpCount(p_collection_name):
    if p_collection_name in collections:
        count = len(collections[p_collection_name])
        print(f"Employee count in '{p_collection_name}': {count}")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")
        
#delEmpById(p_collection_name, p_employee_id)  
def delEmpById(p_collection_name, p_employee_id):
    if p_collection_name in collections:
        collections[p_collection_name] = [emp for emp in collections[p_collection_name] if emp.get('ID') != p_employee_id]
        print(f"Employee with ID {p_employee_id} deleted from '{p_collection_name}'.")
    else:
        print(f"Collection '{p_collection_name}' does not exist.")
# getDepFacet(p_collection_name):  
def getDepFacet(p_collection_name):
    if p_collection_name in collections:
        dep_count = {}
        for emp in collections[p_collection_name]:
            dept = emp.get('Department')
            if dept:
                if dept not in dep_count:
                    dep_count[dept] = 0
                dep_count[dept] += 1
        print("Employee count by department:", dep_count)
    else:
        print(f"Collection '{p_collection_name}' does not exist.")
#driver code 

p_collection_name={"Employee ID" : 1872,
"Full Name": "suri babu",
"Job Title" : "software developer",
"Department":"Engineering",
"Business Unit":"Corporate",
"Gender" : "Male",
"Ethnicity":"Asian",
"Age":24 ,
"Hire Date": "10-10-2024",
"Annual Salary":450000}
print(employ_data.keys())