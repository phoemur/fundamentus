console.log('bla')

var database = firebase.database();

database.ref().child('stocks').once('value').then(function(snapshot){
	console.log(snapshot.val())

	Object.keys(snapshot.val()).forEach(function(key){
		var x = snapshot.val()[key];
		var object = JSON.parse(x);
		console.log(object);
	})

}, function(error){
	console.log("deu erro");
})