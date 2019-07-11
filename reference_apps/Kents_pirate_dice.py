class Jackpot {
  constructor(bet1, bet2, bet3, bet4){
    this.bet1 = bet1;
    this.bet2 = bet2;
    this.bet3 = bet3;
    this.bet4 = bet4;
  }
  winnings(){
    let prize_total = parseInt(this.bet1) + parseInt(this.bet2) + parseInt(this.bet3) + parseInt(this.bet4);
    console.log(`\nTotal in the Jackpot: ${prize_total}`);
    return prize_total
  }
}
function table_count(table_results, jackpot_total) {
  // console.log(`Here's the table results ${table_results}`)
  let one = 0;
  let two = 0;
  let three = 0;
  let four = 0;
  let five = 0;
  let six = 0;
  let dice_val = 0;
  for (i = 0; i < table_results.length; i++) {
    if (table_results[i] == 1) {
      ++one;
      dice_val = 1;
    }
    else if (table_results[i] == 2) {
      ++two;
      dice_val = 2;
    }
    else if (table_results[i] == 3) {
      ++three;
      dice_val = 3;
    }
    else if (table_results[i] == 4) {
      ++four;
      dice_val = 4;
    }
    else if (table_results[i] == 5) {
      ++five;
      dice_val = 5;
    }
    else if (table_results[i] == 6) {
      ++six;
      dice_val = 6;
    }
  }
  // console.log(`\n\tThere were ${one} 1's`)
  // console.log(`\n\tThere were ${two} 2's`)
  // console.log(`\n\tThere were ${three} 3's`)
  // console.log(`\n\tThere were ${four} 4's`)
  // console.log(`\n\tThere were ${five} 5's`)
  // console.log(`\n\tThere were ${six} 6's`)
  let truth = true;
  let num_players = 4;
  let p1_score = 5;
  let p2_score = 5;
  let p3_score = 5;
  let p4_score = 5;
do{
  if(p1_score == 0){
  console.log("\n\t\tYou lose!")
  num_players -= 1;
  break;
  }
  let rand_number_of = Math.floor((Math.random() * 6) + 1);
  let rand_dice_val = Math.floor((Math.random() * 6) + 1);
  if(p2_score > 0){
  let answer = prompt(`\nBlack Beard: "There are ${rand_number_of} ${rand_dice_val}'s'\nDo you agree? (type 'agree' or 'liar')`);
  if (answer == "liar") {
    console.log(`\nBlack Beard said: There are ${rand_number_of} ${rand_dice_val}'s'`);
    for (i = 0; i < table_results.length; i++) {
      if (rand_dice_val == 1) {
        if (rand_number_of > one) {
          console.log("Black Beard lied! They lose a dice.")
           
          p2_score -= 1;
          console.log(`\nBlack Beard has ${p2_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Black Beard told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 2) {
        if (rand_number_of > two) {
          console.log("Black Beard lied! They lose a dice.")
           
          p2_score -= 1;
          console.log(`\nBlack Beard has ${p2_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Black Beard told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 3) {
        if (rand_number_of > three) {
          console.log("Black Beard lied! They lose a dice.")
           
          p2_score -= 1;
          console.log(`\nBlack Beard has ${p2_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Black Beard told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 4) {
        if (rand_number_of > four) {
          console.log("Black Beard lied! They lose a dice.")
           
          p2_score -= 1;
          console.log(`\nBlack Beard has ${p2_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Black Beard told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 5) {
        if (rand_number_of > five) {
          console.log("Black Beard lied! They lose a dice.")
           
          p2_score -= 1;
          console.log(`\nBlack Beard has ${p2_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Black Beard told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 6) {
        if (rand_number_of > six) {
          console.log("Black Beard lied! They lose a dice.")
           
          p2_score -= 1;
          console.log(`\nBlack Beard has ${p2_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Black Beard told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
    }
  }
  }
  // bootstrap Bill
  if(p1_score == 0){
    console.log("\n\t\tYou lose!")
    num_players -= 1;
    break;
  }
  rand_number_of = Math.floor((Math.random() * 6) + 1);
  rand_dice_val = Math.floor((Math.random() * 6) + 1);
 if(p3_score > 0){
  answer = prompt(`\nBootstrap Bill: "There are ${rand_number_of} ${rand_dice_val}'s'\nDo you agree? (type 'agree' or 'liar')`);
  if (answer == "liar") {
    console.log(`\nBootstrap Bill said: There are ${rand_number_of} ${rand_dice_val}'s'`);
    for (i = 0; i < table_results.length; i++) {
      if (rand_dice_val == 1) {
        if (rand_number_of > one) {
          console.log("Bootstrap Bill lied! They lose a dice.")
           
          p3_score -= 1;
          console.log(`\nBootstrap Bill has ${p3_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Bootstrap Bill told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 2) {
        if (rand_number_of > two) {
          console.log("Bootstrap Bill lied! They lose a dice.")
           
          p3_score -= 1;
          console.log(`\nBootstrap Bill has ${p3_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Bootstrap Bill told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 3) {
        if (rand_number_of > three) {
          console.log("Bootstrap Bill lied! They lose a dice.")
           
          p3_score -= 1;
          console.log(`\nBootstrap Bill has ${p3_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Bootstrap Billtold the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 4) {
        if (rand_number_of > four) {
          console.log("Bootstrap Bill lied! They lose a dice.")
           
          p3_score -= 1;
          console.log(`\nBootstrap Bill has ${p3_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Bootstrap Bill told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 5) {
        if (rand_number_of > five) {
          console.log("Bootstrap Bill lied! They lose a dice.")
           
          p3_score -= 1;
          console.log(`\nBootstrap Bill has ${p3_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Bootstrap Bill told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 6) {
        if (rand_number_of > six) {
          console.log("Bootstrap Bill lied! They lose a dice.")
           
          p3_score -= 1;
          console.log(`\nBootstrap Bill has ${p3_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Bootstrap Bill told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
    }
  }
  // Davy Jones
  if(p1_score == 0){
    console.log("\n\t\tYou lose!")
    num_players -= 1;
    break;
  }
  rand_number_of = Math.floor((Math.random() * 6) + 1);
  rand_dice_val = Math.floor((Math.random() * 6) + 1);
 if(p4_score > 0){
  answer = prompt(`\nDavy Jones: "There are ${rand_number_of} ${rand_dice_val}'s'\nDo you agree? (type 'agree' or 'liar')`);
  if (answer == "liar") {
    console.log(`\nDavy Jones said: There are ${rand_number_of} ${rand_dice_val}'s'`);
    for (i = 0; i < table_results.length; i++) {
      if (rand_dice_val == 1) {
        if (rand_number_of > one) {
          console.log("Davy Jones lied! They lose a dice.")
           
          p4_score -= 1;
          console.log(`\nDavy Jones has ${p4_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Davy Jones told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 2) {
        if (rand_number_of > two) {
          console.log("Davy Jones lied! They lose a dice.")
           
          p4_score -= 1;
          console.log(`\nDavy Jones has ${p4_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Davy Jones told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 3) {
        if (rand_number_of > three) {
          console.log("Davy Jones lied! They lose a dice.")
           
          p4_score -= 1;
          console.log(`\nDavy Jones has ${p4_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Davy Jones the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 4) {
        if (rand_number_of > four) {
          console.log("Davy Jones lied! They lose a dice.")
           
          p4_score -= 1;
          console.log(`\nDavy Jones has ${p4_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Davy Jones told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 5) {
        if (rand_number_of > five) {
          console.log("Davy Jones lied! They lose a dice.")
           
          p4_score -= 1;
          console.log(`\nDavy Jones has ${p4_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Davy Jones told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
      else if (rand_dice_val == 6) {
        if (rand_number_of > six) {
          console.log("Davy Jones lied! They lose a dice.")
           
          p4_score -= 1;
          console.log(`\nDavy Jones has ${p4_score} dice left.`)
          truth = false;
          break;
        }
        else {
          console.log("Davy Jones told the truth! You lose a dice.")
           
          p1_score -= 1;
          console.log(`You have ${p1_score} dice left.`)
          break;
        }
      }
    }
  }
 }
  if(p1_score == 0){
    console.log("\n\t\tYou lose!")
    num_players -= 1;
    break;
  }
  else if(p2_score == 0){
    console.log("\n\t\tBlack Beard loses!")
    num_players -+ 1;
  }
  else if(p3_score == 0){
    console.log("\n\t\tBootstrap Bill loses!")
    num_players -+ 1;
  }
  else if(p4_score == 0){
    console.log("\n\t\tDavy Jones loses!")
    num_players -+ 1;
  }
  if(p2_score == 0 && p3_score == 0 && p4_score == 0){
    console.log(`\n\t\tYou Win!\n\t\tYou get ${jackpot_total} in gold!`);
    let win = true;
    return win;
    break;
  }
 }
  }while(num_players > 1);
  console.log("\t\tGame Over");
}
function roll_dice(player, num_dice, sides) {
  let dice_array = []
  for (i = 1; i < num_dice + 1; i++) {
    roll = Math.floor((Math.random() * sides) + 1);
    dice_array.push(roll)
  }
  // console.log(`\n\t${player} rolled.... ${dice_array}\n\t Dice remaining: ${num_dice}\n`);
  return dice_array;
}
let sides = 6;
let num_dice = 5;
const playerOne = "You";
const playerTwo = "Black Beard";
const playerThree = "Bootstrap Bill";
const playerFour = "Davy Jones";
let answer = "";
let playerOne_cup = roll_dice(playerOne, num_dice, sides);
let playerTwo_cup = roll_dice(playerTwo, num_dice, sides);
let playerThree_cup = roll_dice(playerThree, num_dice, sides);
let playerFour_cup = roll_dice(playerFour, num_dice, sides);
let table_results = playerOne_cup.concat(playerTwo_cup, playerThree_cup, playerFour_cup);
let p1_bet = prompt("How many gold coins would you like to bet?\nThis will be added to the jackpot. Winner takes all!")
let p2_bet = Math.floor((Math.random() * 500) + 1);
let p3_bet = Math.floor((Math.random() * 500) + 1);
let p4_bet = Math.floor((Math.random() * 500) + 1);
console.log(`You bet: ${p1_bet}\nBlack Beard bet: ${p2_bet}\nBootstrap Bill bet: ${p3_bet}\nDavy Jones bet: ${p4_bet}`)
let jackpot_var = new Jackpot(p1_bet, p2_bet, p3_bet, p4_bet);
let jackpot_total = (jackpot_var.winnings());
table_count(table_results, jackpot_total);
// X all players roll their dice 
// X all players start with 5 dice
// X view your dice random for all num_dice and display
// X players take turns betting 2 2's 3 1's etc.
// X player decides if they agree or call liar for each players turn
// X if the player that calls liar is true, then they win and the current player loses 1 dice.
// X if the player who called lair is false, then they lose 1 dice.
// X combining the arrays to count up how many of each number there are on the table
// X make bets random between 100 and 500 gold and player one whatever they want.
// X winner takes the jackpot