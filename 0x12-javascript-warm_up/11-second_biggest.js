#!/usr/bin/node
const argArray = process.argv.slice(2);
function secBiggest(array)
{
	if (array[2] === undefined || array[2] === 1)
	{
		return (0);
	}
	else
	{
		array.sort((x, y) => x - y);
		array.pop();
		return (array.pop());
	}
}
console.log(secBiggest(argArray));
