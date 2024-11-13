pragma solidity >=0.7.0 <0.9.0;

contract StudentManagement {
	
	struct Student {
		uint256 stud_id;
		string Name;
		string Department;
	}

	Student[] private Students; // Made it private for encapsulation
	
	constructor() payable {}
	
	function addStudent(uint256 stud_id, string memory Name, string memory Department) public {
		Student memory stud = Student(stud_id, Name, Department);
		Students.push(stud);
	}

	function getStudent(uint256 stud_id) public view returns(string memory, string memory) {
		for (uint256 i = 0; i < Students.length; i++){
			if(Students[i].stud_id == stud_id){
				return (Students[i].Name, Students.Department);
			}
		}
		return("Name not Found!", "Department not Found!");
	}
	
	recieve() external payable {}

	fallback() external payable {
		Students.push(Student(7,"XYZ", "Mech"));
	}


}
