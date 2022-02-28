#!/usr/bin/node
const arg = parseInt(process.argv[2], 10)
if (isNaN(arg))
{
	console.log('Missing number of occurrences');
}
else
{
	for (let a = arg; a > 0; a--)
	{
		console.log('C is fun');
	}
}
