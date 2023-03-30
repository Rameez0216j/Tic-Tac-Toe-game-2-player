const boxes=document.querySelectorAll(".box");
const gameInfo=document.querySelector(".game-info");
const newGameBtn=document.querySelector(".New-game-btn");

let currentPlayer;
let gameGrid;

const winningPositions = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]; // ; is important

function initGame(){
    currentPlayer='X';
    gameGrid=["","","","","","","","",""];
    boxes.forEach((box,index)=>{
        box.innerText="";


        // remove current won cells green color 
        box.classList=`box box${index+1}`;
        // boxes[index].classList=`box box${index+1}`;


        // enabling pointer events
        box.style.pointerEvents="all";
        // boxes[index].style.pointerEvents="all";
    });
    newGameBtn.classList.remove("active");
    gameInfo.innerText=`Current Player - ${currentPlayer}`;
}

initGame();

function swapTurn(){
    if(currentPlayer==="X"){
        currentPlayer="O";
    }
    else{
        currentPlayer="X";
    }
    // updating above notification 
    gameInfo.innerText=`Current Player - ${currentPlayer}`;

    // Now integration alpha beta pruning for computer as 'O'
}



function handleClick(index){
    if(gameGrid[index]===""){
        gameGrid[index]=currentPlayer;
        boxes[index].innerText=currentPlayer;
        boxes[index].style.pointerEvents="none";

        swapTurn();
        checkGameOver();
    }
}

function checkGameOver(){
    let winner="";
    winningPositions.forEach((pos)=>{
        if((gameGrid[pos[0]]!==""  && gameGrid[pos[1]]!=="" && gameGrid[pos[2]]!=="") && 
        (gameGrid[pos[0]]===gameGrid[pos[1]]  && gameGrid[pos[1]]===gameGrid[pos[2]])){

            // winner=boxes[pos[0]].innerText;
            winner=gameGrid[pos[0]];
            // Winning box color change
            boxes[pos[0]].classList.add("win");
            boxes[pos[1]].classList.add("win");
            boxes[pos[2]].classList.add("win");

            // Disabling pointer events for stopping the game
            boxes.forEach((box)=>{
                box.style.pointerEvents="none";
            });
        }
    });


    if(winner!==""){
        gameInfo.innerText=`Winner - ${winner}`;
        newGameBtn.classList.add("active");
        return; // for avoiding unnecessary code check below
    }


    let count=0;
    // gameGrid.forEach((box)=>{
    //     if(box!==""){
    //         count++;
    //     }
    // });
    boxes.forEach((box)=>{
        if(box.innerText!==""){
            count++;
        }
    });

    if(count==9){
        gameInfo.innerText=`Game Tied !`;
        newGameBtn.classList.add("active");
    }
}


boxes.forEach((box,index)=>{
    box.addEventListener("click",()=>{
        handleClick(index);
    });
});

newGameBtn.addEventListener("click",initGame);