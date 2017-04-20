console.log('bla')

var database = firebase.database();

var arrayStocksHistory = [];

database.ref().child('stocks').once('value').then(function(snapshot){
	// console.log(snapshot.val())

	Object.keys(snapshot.val()).forEach(function(key){
		// console.log(snapshot.val()[key])
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

	// console.log(arrayStocksHistory);
	buildTable(arrayStocksHistory[0]);
	hideLoading();

}, function(error){
	console.log("deu erro");
})


var hideLoading = function(){
	$('#loading-whell').addClass("hidden");
	$('#info').removeClass("hidden");
}

var buildTable = function(data){
	// Sort elements by score
	[].slice.call(data).sort(function(a, b){
		var nota1 = 0;
		var nota2 = 0;
		Object.keys(a).forEach(function(key){
			nota1 = a[key]["nota"];
		})
		Object.keys(b).forEach(function(key){
			nota2 = b[key]["nota"];
		})
		return nota2 - nota1;
	})

	var txt = "";
	Object.keys(data).forEach(function(key){
		if(parseInt(key) < 1000){
			Object.keys(data[key]).forEach(function(stock){
				var stockInfo = {
					stockName: stock,
					nota: data[key][stock]["nota"],
					cotacao: data[key][stock]["cotacao"],
					patLiq: data[key][stock]["Pat.Liq"],
					LiqCorr: data[key][stock]["Liq.Corr."],
					ROE: data[key][stock]["ROE"],
					DivPat: data[key][stock]["Div.Brut/Pat."],
					Cresc5: data[key][stock]["Cresc.5a"],
					PVP: data[key][stock]["P/VP"],
					PL: data[key][stock]["P/L"],
					Div: data[key][stock]["DY"]
				}
				// console.log(stockInfo);

				var stockLine = "<tr>" + 
								"<td class='stock'>" + stockInfo.stockName + "</td>" + 
				            	"<td>" + stockInfo.nota + "</td>" + 
				            	"<td>" + stockInfo.cotacao + "</td>" + 
				            	"<td>" + stockInfo.patLiq + "</td>" + 
				            	"<td>" + stockInfo.LiqCorr + "</td>" + 
				            	"<td>" + stockInfo.ROE + "</td>" + 
				            	"<td>" + stockInfo.DivPat + "</td>" + 
				            	"<td>" + stockInfo.Cresc5 + "</td>" + 
				            	"<td>" + stockInfo.PVP + "</td>" + 
				            	"<td>" + stockInfo.PL + "</td>" + 
				            	"<td>" + stockInfo.Div + "</td>" + 
				        		"</tr>";
				// console.log(stockLine);

				txt += stockLine;
			});
		}
	})
	
	$("#resultado").append(txt)




}