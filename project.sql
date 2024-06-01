CREATE DATABASE EMPLOYEE;
USE EMPLOYEE;
SELECT*FROM DATA_SCIENCE_TEAM;
SELECT*FROM EMP_RECORD_TABLE;
SELECT*FROM PROJ_TABLE;
DESCRIBE DATA_SCIENCE_TEAM;
DESCRIBE EMP_RECORD_TABLE;
DESCRIBE PROJ_TABLE;
select count(PROJ_NAME) AS TOTAL_PROJECTS from PROJ_TABLE;

/* 3. Write a query to fetch EMP_ID, FIRST_NAME, LAST_NAME, GENDER, and DEPARTMENT 
from the employee record table, and make a list of employees and details of their department*/

SELECT  EMP_ID, FIRST_NAME,LAST_NAME, GENDER,DEPT FROM EMP_RECORD_TABLE;

/* 4.Write a query to fetch EMP_ID, FIRST_NAME, LAST_NAME, GENDER, DEPARTMENT, and EMP_RATING if the EMP_RATING is:
• less than two
• greater than four
• between two and four */



SELECT EMP_ID,FIRST_NAME,LAST_NAME,GENDER,DEPT,EMP_RATING FROM EMP_RECORD_TABLE
WHERE EMP_RATING<2;

SELECT EMP_ID,FIRST_NAME,LAST_NAME,GENDER,DEPT,EMP_RATING FROM EMP_RECORD_TABLE
WHERE EMP_RATING>4;

SELECT EMP_ID,FIRST_NAME,LAST_NAME,GENDER,DEPT,EMP_RATING FROM EMP_RECORD_TABLE
WHERE EMP_RATING BETWEEN 2 AND 4;

/* 5. Write a query to concatenate the FIRST_NAME and the LAST_NAME of employees in the 
Finance department from the employee table and then give the resultant column alias as NAME.*/

SELECT CONCAT(FIRST_NAME,'  ',LAST_NAME) AS NAME,DEPT FROM EMP_RECORD_TABLE WHERE DEPT='FINANCE';

/* 6. Write a query to list only those employees who have someone reporting to them. Also, show 
the number of reporters (including the President). */

SELECT MANAGER_ID,COUNT(EMP_ID) AS EMP_COUNT FROM EMP_RECORD_TABLE GROUP BY MANAGER_ID ORDER BY EMP_COUNT ;

/* 7. Write a query to list down all the employees from the healthcare and finance departments 
using union. Take data from the employee record table.*/

SELECT*FROM EMP_RECORD_TABLE WHERE DEPT='HEALTHCARE' UNION SELECT*FROM EMP_RECORD_TABLE WHERE DEPT='FINANCE';

/* 8. Write a query to list down employee details such as EMP_ID, FIRST_NAME, LAST_NAME, 
ROLE, DEPARTMENT, and EMP_RATING grouped by dept. Also include the respective employee 
rating along with the max emp rating for the department.*/

SELECT EMP_ID,FIRST_NAME,LAST_NAME,ROLE,DEPT,EMP_RATING,MAX(EMP_RATING)
FROM EMP_RECORD_TABLE GROUP BY EMP_ID,FIRST_NAME,LAST_NAME,ROLE,DEPT,EMP_RATING;



/* 9. Write a query to calculate the minimum and the maximum salary of the employees in each 
role. Take data from the employee record table. */

SELECT MIN(SALARY),MAX(SALARY),ROLE FROM EMP_RECORD_TABLE GROUP BY ROLE;

/* 10. Write a query to assign ranks to each employee based on their experience. Take data from 
the employee record table. */

SELECT*FROM EMP_RECORD_TABLE ORDER BY EXP DESC;

/* 11. Write a query to create a view that displays employees in various countries whose salary is 
more than six thousand. Take data from the employee record table. */

CREATE VIEW EMP AS SELECT*FROM EMP_RECORD_TABLE WHERE SALARY>6000;
SELECT*FROM EMP ORDER BY SALARY;

/* 12. Write a nested query to find employees with experience of more than ten years. Take data 
from the employee record table.*/

SELECT*FROM EMP_RECORD_TABLE WHERE EXP IN (SELECT EXP FROM EMP_RECORD_TABLE WHERE EXP>10);

/* 13. Write a query to create a stored procedure to retrieve the details of the employees whose 
experience is more than three years. Take data from the employee record table.*/

CALL EMPLOYEES;  
CALL EMPLOYEE ;

/* 14. Write a query using stored functions in the project table to check whether the job profile 
assigned to each employee in the data science team matches the organization’s set standard.
The standard being:
For an employee with experience less than or equal to 2 years assign 'JUNIOR DATA SCIENTIST',
For an employee with the experience of 2 to 5 years assign 'ASSOCIATE DATA SCIENTIST',
For an employee with the experience of 5 to 10 years assign 'SENIOR DATA SCIENTIST',
For an employee with the experience of 10 to 12 years assign 'LEAD DATA SCIENTIST',
For an employee with the experience of 12 to 16 years assign 'MANAGER'. */


/* 15. Create an index to improve the cost and performance of the query to find the employee 
whose FIRST_NAME is ‘Eric’ in the employee table after checking the execution plan. */

ALTER TABLE EMP_RECORD_TABLE MODIFY FIRST_NAME VARCHAR(30);
CREATE INDEX FIRST_NAME ON EMP_RECORD_TABLE(FIRST_NAME);
SELECT*FROM EMP_RECORD_TABLE WHERE FIRST_NAME='ERIC';

/* 16. Write a query to calculate the bonus for all the employees, based on their ratings and 
salaries (Use the formula: 5% of salary * employee rating).*/

SELECT FIRST_NAME,EMP_RATING,SALARY,((SALARY) *( EMP_RATING)) *(0.05) AS BONUS FROM EMP_RECORD_TABLE GROUP BY FIRST_NAME,EMP_RATING,SALARY;

/*17. Write a query to calculate the average salary distribution based on the continent and country. 
Take data from the employee record table*/

SELECT CONTINENT,COUNTRY,AVG(SALARY) AS AVG_SALARY
 FROM EMP_RECORD_TABLE GROUP BY CONTINENT,COUNTRY; 


CREATE TABLE HP(Name varchar(20) NOT NULL,Age int);
describe HP;
