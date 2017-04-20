console.log('bla')

var database = firebase.database();

var arrayStocksHistory = [];

database.ref().child('stocks').once('value').then(function(snapshot){
	console.log(snapshot.val())

	Object.keys(snapshot.val()).forEach(function(key){
		var object = JSON.parse(snapshot.val()[key]);
		arrayStocksHistory.push(object)
		// console.log(object);
	})

	// Sort by date, the first one will be the newest
	arrayStocksHistory.sort(function(a,b){
		var date1 = new Date(a.date);
		var date2 = new Date(b.date);
		return date2 - date1;
	})

	console.log(arrayStocksHistory);
	hideLoading();

}, function(error){
	console.log("deu erro");
})


var hideLoading = function(){
	$('#loading-whell').css('display', "none");
	$('#info').css('display', "block");
}