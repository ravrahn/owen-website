var tileBeingAdded = false;

var players = ["red", "blue"];
var currentPlayer = players[0];

var board = [[],[],[],[],[],[],[]];

var lines = [
                // Vertical lines
                [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5]],
                [[1,0],[1,1],[1,2],[1,3],[1,4],[1,5]],
                [[2,0],[2,1],[2,2],[2,3],[2,4],[2,5]],
                [[3,0],[3,1],[3,2],[3,3],[3,4],[3,5]],
                [[4,0],[4,1],[4,2],[4,3],[4,4],[4,5]],
                [[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]],
                [[6,0],[6,1],[6,2],[6,3],[6,4],[6,5]],
                // Horizontal Lines
                [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]],
                [[0,1],[1,1],[2,1],[3,1],[4,1],[5,1],[6,1]],
                [[0,2],[1,2],[2,2],[3,2],[4,2],[5,2],[6,2]],
                [[0,3],[1,3],[2,3],[3,3],[4,3],[5,3],[6,3]],
                [[0,4],[1,4],[2,4],[3,4],[4,4],[5,4],[6,4]],
                [[0,5],[1,5],[2,5],[3,5],[4,5],[5,5],[6,5]],
                // Diagonal Right Lines (/)
                [[0,2],[1,3],[2,4],[3,5]],
                [[0,1],[1,2],[2,3],[3,4],[4,5]],
                [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5]],
                [[1,0],[2,1],[3,2],[4,3],[5,4],[6,5]],
                [[2,0],[3,1],[4,2],[5,3],[6,4]],
                [[3,0],[4,1],[5,2],[6,3]],
                // Diagonal Left Lines (\)
                [[0,3],[1,2],[2,1],[3,0]],
                [[0,4],[1,3],[2,2],[3,1],[4,0]],
                [[0,5],[1,4],[2,3],[3,2],[4,1],[5,0]],
                [[1,5],[2,4],[3,3],[4,2],[5,1],[6,0]],
                [[2,5],[3,4],[4,3],[5,2],[6,1]],
                [[3,5],[4,4],[5,3],[6,2]]
            ];


function isLegal(column) {
    rows = $(".board tr");

    var isLegal = false;

    // for each tile in the column, check if it's empty
    rows.each(function() {
        var col = $(this).children("." + column);
        var tile = col.children(".tile");
        if (!tile.hasClass("blue") && !tile.hasClass("red")) {
            isLegal = true;
        }
    });

    return isLegal;
}

function addTile(column) {
    tileBeingAdded = true;

    //add the tile to the html board
    var tile = null;

    // find the lowest tile to put a piece in
    rows.each(function() {
        var col = $(this).children("." + column);
        var tempTile = col.children(".tile");
        if (!tempTile.hasClass("blue") && !tempTile.hasClass("red")) {
            tile = tempTile;
        }
    });

    var top = Math.random() * 7 + 1;
    var left = Math.random() * 2 + 4.5;

    tile.html("<div class=\"" + currentPlayer + " circle\" style=\"top: -" + top + "rem; left: -" + left +"rem;\"></div>");

    var circle = tile.children(".circle");

    setTimeout(function() {
        circle.css("height", "18rem");
        circle.css("width", "18rem");
        circle.css("margin-top", "0");
        circle.css("opacity", "1");
    },0);

    setTimeout(function() {
        tile.addClass(currentPlayer);
        tile.html("");
        tileBeingAdded = false;
    },300);

    // add the tile to the board array
    var colNum = parseInt(column.slice(-1));
    if (board[colNum].length < 6) {
        board[colNum].push(currentPlayer);
    }

    victory = checkVictory(currentPlayer);

    if (!victory) {
        if (players.indexOf(aiPlayer) != -1 && aiPlayer != currentPlayer) {
            setTimeout(aiMove, 500);
        }

        // toggle player
        setTimeout(function() {
            currentPlayer = (currentPlayer == players[1]) ? players[0] : players[1]
        }, 350);
    }

}

function checkVictory(player) {
    var victory = false;

    var stalemate = true;
    for (var col=0; col < 7; col++) {
        if (board[col].length != 6) {
            stalemate = false;
        }
    }

    // check no victory in each column
    for (var line=0; line < lines.length; line++) {
        var lineArr = lines[line];

        var chain = 0;
        
        for (var tile=0; tile < lineArr.length; tile++) {
            var tileArr = lineArr[tile];

            var col = tileArr[0];
            var row = tileArr[1];

            if (board[col][row] === player) {
                chain++;
            } else {
                chain = 0;
            }
            if (chain === 4) {
                victory = true;
            }
        }
    }

    // show victory screen if victorious
    if (victory) {
        $(".victory-overlay").css("visibility", "visible");
        $(".victory-text").html(player[0].toUpperCase() + player.slice(1) + " wins!");
    } else if (stalemate) {
        $(".victory-overlay").css("visibility", "visible");
        $(".victory-text").html("Stalemate.");
    } 

    return victory;
}

$("td").hover(function() {
    var col = $(this).attr("class");

    rows = $(".board tr");

    rows.each(function() {
        $(this).children("." + col).css("background-color", "#EEE");
    })
}, function() {
    var col = $(this).attr("class");

    rows = $(".board tr");

    rows.each(function() {
        $(this).children("." + col).css("background-color", "white");
    })
});

var humanPlayer = players[0];

$("td").click(function() {
    if (isLegal($(this).attr("class")) && !tileBeingAdded) {
        if (humanPlayer == currentPlayer) {
            addTile($(this).attr("class"));
        }
    }
});