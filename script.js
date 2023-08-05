const taxRate = 0.15;
fetch('./data.json')
  .then(response => response.json())
  .then(data => {
    // Loop through an array in the JSON data
    data.forEach(person => {
      console.log(getFullName(person));
      console.log(getAge(person));
      console.log(getSex(person)),
      console.log(getJobTitle(person)),
      console.log(getEthnicity(person)),
      console.log(getMaritalStatus(person)),
      console.log(getSalary(person)),
      console.log(getSalaryTaxes(person));
    });
  })
  
  .catch(error => {
    // Handle any errors that occur while fetching the file
    console.error(error);
  });
  
  function getFullName(person){
    return `${person.firstName} ${person.lastName}`;
  }

  function getAge(person){
    const birthYear = new Date(person.birthday).getFullYear();
    const currentYear = new Date().getFullYear();
    const age = currentYear - birthYear;
    return `${person.firstName} is ${age} years old.`;
  }
  
  function getSex(person){
    return person.sex;
  }

  function getJobTitle(person){
    return person.jobTitle;
  }

  function getEthnicity(person){
    return person.ethnicity;
  }

  function getMaritalStatus(person){
    return person.maritalStatus;
  }

  function getSalary(person){
    return person.salary;
  }

  function getSalaryTaxes(person){
    return person.salary * taxRate;
  }


