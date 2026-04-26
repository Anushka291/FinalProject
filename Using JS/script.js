let students = [];

function renderList() {
    let list = document.getElementById("list");
    list.innerHTML = "";

    students.forEach((student, index) => {
        let li = document.createElement("li");

        li.innerHTML = `
            Name: ${student.name} | PRN: ${student.prn} | Course: ${student.course}
            <button onclick="editStudent(${index})">Edit</button>
            <button onclick="deleteStudent(${index})">Delete</button>
        `;

        list.appendChild(li);
    });
}

// CREATE
function addStudent() {
    let name = document.getElementById("name").value;
    let prn = document.getElementById("prn").value;
    let course = document.getElementById("course").value;

    if (!name || !prn || !course) return;

    students.push({ name, prn, course });

    console.log("CREATED");   // 👈 IMPORTANT

    document.getElementById("name").value = "";
    document.getElementById("prn").value = "";
    document.getElementById("course").value = "";

    renderList();
}

// UPDATE
function editStudent(index) {
    let newName = prompt("Enter new name:");
    let newPRN = prompt("Enter new PRN:");
    let newCourse = prompt("Enter new Course:");

    if (newName && newPRN && newCourse) {
        students[index] = {
            name: newName,
            prn: newPRN,
            course: newCourse
        };

        console.log("UPDATED");   // 👈 IMPORTANT

        renderList();
    }
}

// DELETE
function deleteStudent(index) {
    students.splice(index, 1);

    console.log("DELETED");   // 👈 IMPORTANT

    renderList();
}