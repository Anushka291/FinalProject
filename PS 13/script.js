let students = [];
let editIndex = -1;

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

// CREATE / UPDATE
function addStudent() {
    let name = document.getElementById("name").value;
    let prn = document.getElementById("prn").value;
    let course = document.getElementById("course").value;

    if (!name || !prn || !course) return;

    if (editIndex === -1) {
        students.push({ name, prn, course });
        console.log("CREATED");
    } else {
        students[editIndex] = { name, prn, course };
        console.log("UPDATED");
        editIndex = -1;
    }

    document.getElementById("name").value = "";
    document.getElementById("prn").value = "";
    document.getElementById("course").value = "";

    renderList();
}

// EDIT → fill fields instead of prompt
function editStudent(index) {
    let student = students[index];

    document.getElementById("name").value = student.name;
    document.getElementById("prn").value = student.prn;
    document.getElementById("course").value = student.course;

    editIndex = index;
}

// DELETE
function deleteStudent(index) {
    students.splice(index, 1);
    console.log("DELETED");
    renderList();
}