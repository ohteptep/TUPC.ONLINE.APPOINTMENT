$('#bookAlumnus1').click(function(){
    firstname = $('#fname').val();
    lastname = $('#lname').val();
    email = $('#emails').val();
    idstudent = $('#student_id').val();
    courses = $('#course').val();
    years = $('#year').val();
    date = $('#dates').val();
    departments = $('#depts').val();
    purposes = $('#purpose').val();

    if (firstname == "" || lastname == "" || email == "" || idstudent == "" || years == "" || date == "" || courses == "" || departments == "" || purposes == ""){
        alert('Error please fill up the necessary information neededddddddddddddddddddd');
    }
    else{
        alert('Successfully added. Please wait for the confirmation through email!');
        
    }

})