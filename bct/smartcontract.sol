pragma solidity >=0.7.0 <0.9.0;

contract Bank {

    // Mapping to store user account balances and existence
    mapping(address => uint) public user_account;
    mapping(address => bool) public user_exist;

    // Constructor to accept the initial deposit
    constructor() payable {
        require(msg.value > 0, "Initial deposit must be greater than 0");
        user_account[msg.sender] = msg.value;
        user_exist[msg.sender] = true;
    }

    // Modifier to ensure only existing account holders can call certain functions
    modifier onlyExistingAccount() {
        require(user_exist[msg.sender], "Account not created!");
        _;
    }

    // Function to create an account with an initial deposit
    function create_account() public payable returns(string memory) {
        require(!user_exist[msg.sender], "Account already created!");
        require(msg.value > 0, "Initial deposit must be greater than 0");
        user_account[msg.sender] = msg.value;
        user_exist[msg.sender] = true;
        return "Account created";
    }

    // Function to deposit funds into an existing account
    function deposit() public payable onlyExistingAccount returns(string memory) {
        require(msg.value > 0, "Amount should be greater than 0");
        user_account[msg.sender] += msg.value;
        return "Amount deposited successfully";
    }

    // Function to withdraw funds from an existing account
    function withdraw(uint amount) public onlyExistingAccount returns(string memory) {
        require(amount > 0, "Amount should be greater than 0");
        require(user_account[msg.sender] >= amount, "Insufficient balance");
        user_account[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
        return "Amount withdrawn successfully";
    }

    // Function to check the account balance of the caller
    function account_balance() public view onlyExistingAccount returns(uint) {
        return user_account[msg.sender];
    }

    // Function to check if the caller's account exists
    function account_exists() public view returns(bool) {
        return user_exist[msg.sender];
    }
}

