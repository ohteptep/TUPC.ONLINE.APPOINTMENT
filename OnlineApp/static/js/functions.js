$(document).ready(function(){

    //Signup Admin
    $('#createAdmin').click(function(){
        department = $('#dept').val();
        passw = $('#password').val();

        if (passw == ""){
            alert('Error please fill up the necessary information needed')
        }
        

    })
    
    //Login Admin
    $('#loginAdmin').click(function(){
        department = $('#dept').val();
        passw = $('#password').val();

        if (passw == ""){
            alert('Error please fill up the necessary information needed')
        }

    })

    //Login Student
    $('#loginS').click(function(){
        user = $('#loginStudent').val();
        passw = $('#passwordStudent').val();

        if (passw == "" || user == ""){
            alert('Error please fill up the necessary information needed')
        }
        

    })

    //Signup Student
    $('#studentCreate').click(function(){
        mail = $('#emails').val();
        pasw = $('#passwords').val();
        repass = $('#re-password').val();

        if (pasw == "" || repass == "" || mail == ""){
            alert('Error please fill up the necessary information needed');
        }else if(pasw != repass){
            alert('Error in password!')
        }
        

    })

    

    //Alumnus Form
    $('#bookAlumnus').click(function(){
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
            alert('Error please fill up the necessary information needed');
        }
        else{
            alert('Successfully added. Please wait for the confirmation through email!');
            
        }

    })

    //Student Form
    $('#bookStudent').click(function(){
        firstname = $('#fnames').val();
        lastname = $('#lnames').val();
        email = $('#emailss').val();
        idstudent = $('#idstudent').val();
        courses = $('#course').val();
        years = $('#years').val();
        date = $('#datess').val();
        departments = $('#depts').val();
        purposes = $('#purposes').val();

        console.log(firstname)
        console.log(lastname)
        console.log(email)
        console.log(idstudent)
        console.log(courses)
        console.log(years)
        console.log(date)
        console.log(departments)
        console.log(purposes)
        if (firstname == "" || lastname == "" || email == "" || idstudent == "" || years == "" || date == "" || courses == "" || departments == "" || purposes == ""){
            alert('Error please fill up the necessary information needed');
        }
        else{
            alert('Successfully added. Please wait for the confirmation through email!');
            
        }

    })

    //Guardian Form
    $('#bookGuardian').click(function(){
        guardian = $('#guardians').val();
        firstname = $('#ffname').val();
        lastname = $('#llname').val();
        email = $('#eemails').val();
        idstudent = $('#studentid').val();
        courses = $('#courses').val();
        date = $('#datesss').val();
        departments = $('#depts').val();
        purposes = $('#purpos').val();


        console.log(guardian)
        console.log(firstname)
        console.log(lastname)
        console.log(email)
        console.log(idstudent)
        console.log(courses)
        console.log(date)
        console.log(departments)
        console.log(purpos)

        if (guardian == "" || firstname == "" || lastname == "" || email == "" || idstudent == "" || years == "" || date == "" || courses == "" || departments == "" || purposes == ""){
            alert('Error please fill up the necessary information needed');
        }
        else{
            alert('Successfully added. Please wait for the confirmation through email!');
            
        }

    })
})