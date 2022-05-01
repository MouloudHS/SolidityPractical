// SPDX-License-Identifier: MIT

pragma solidity 0.8.7;

// Import chainlink datafeeds...
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract FundMe {

    address public owner;
    address[] public funders;
    mapping(address => uint256) public amoutToAddress;
    
    // Define the owner of the contract (First to deploy)
    constructor() { owner = msg.sender; }

    // Getting price using chainlink datafeeds
    function getPrice() public view returns(uint256) {
        AggregatorV3Interface priceFeed = AggregatorV3Interface(0x8A753747A1Fa494EC906cE90E9f37563A8AF630e);
        (,int256 answer,,,) = priceFeed.latestRoundData();
        return uint256(answer * 10000000000);
    }

    // Getting conversion rate
    function getConversionRate(uint256 ethAmount) public view returns(uint256) {
        uint256 price = getPrice();
        uint256 priceUSD = (price * ethAmount)/1000000000000000000;
        return priceUSD;
    }


    function fund() public payable {
        uint256 minUSD = 50 * 10**18;
        require(getConversionRate(msg.value) >= minUSD, "You need to spend more ETH!");
        amoutToAddress[msg.sender] += msg.value;
        funders.push(msg.sender);
    }

    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }

    function withdraw() public onlyOwner payable {
        payable(msg.sender).transfer(address(this).balance);
        for (uint256 fundersIndex = 0; fundersIndex <= funders.length; fundersIndex++) {
            address funder = funders[fundersIndex];
            amoutToAddress[funder] = 0;

        funders = new address[](0); 
        }
    }
}