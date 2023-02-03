This code demonstrates patch and delete requests of FastAPI via python
It also examines use of lists, dictionaries and HTTP exceptions -> particularly 404 not found exceptions

the function update_by_id() will search for an id match and update the isDone characteristic of the Todo to True, if no match is found a 404 not found exception will raised

the function delete_by_id() will search for an id match in the fake_database and remove it from the database. If no match is found a 404 not found exception will be raised

Blaziken