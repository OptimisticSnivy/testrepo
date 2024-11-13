// SPDX-License-Identifier: MIT 

pragma solidity >=0.7.0 <0.9.0;

contract Bank{
	mapping(address=>uint) public user_account;
	mapping(address=>bool) public user_exists;
	
	constructor() payable {
		require(msg.value > 0, "Initial Deposit should be greater than 0");
		user_account[msg.sender] = msg.value;
		user_exists[msg.sender] = true;
	}

	modifier onlyExistingAccount() {
		require(user_exists[msg.sender], "Account is not created!");
		_;
	}

	function create_account() public payable returns(string memory) {
		require(!user_exists[msg.sender],"Account already created!");
		require(msg.value > 0, "Initial Deposit should be greater than 0");
		user_account[msg.sender] = msg.value;
		user_exists[msg.sender] = true;
		return "Account created!";
	}

	function deposit() public payable onlyExistingAccount returns(string memory) {
		require(msg.value > 0, "Amount should be greater than 0");
		user_account[msg.sender] += msg.value;
		return "Amount deposited!"
	}

	function withdraw(uint amount) public onlyExistingAccount returns(string memory) {
		require(amount > 0, "Amount should be greater than 0");
		require(user_account[msg.sender] >= amount , "Insufficient Balance!");
		user_account[msg.sender] -= amount;
		payable(msg.sender).transfer(amount);
		return "Amount withdrawn!";
	}

	function account_balance() public view onlyExistingAccount returns(uint) {
		return user_account[msg.sender];
	}

	function account_exists() public view returns(bool) {
		return user_exists[msg.sender];
	} 


}
