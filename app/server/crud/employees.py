from server.database import employee_collection, employee_helper

# List all employees present in the database
async def list_employees(filters=None):
    employees = []
    async for employee in employee_collection.find(filters):
        employees.append(employee_helper(employee))
    return employees