#!/usr/bin/node
const arg = parseInt(process.argv[2], 10);
if (isNaN(arg))
{
	console.log('Missing size');
}
else
{
	for (let a = 0; a < arg; a++)
	{
		console.log('X'.repeat(arg));
	}
}
