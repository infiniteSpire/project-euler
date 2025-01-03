pub fn solve() {
  println!("Problem nº1: Multiples of 3 or 5");
  println!("Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.");

  let list: Vec<i32> = (1..=1000).collect();
  let mut new_list: Vec<i32> = Vec::new();
  for number in &list {
    if number % 3 == 0 {
      new_list.push(*number)
    } else if number % 5 == 0 {
      new_list.push(*number)
    }
  }
  let mut total = 0;
  for number in &new_list {
    total = total + number
  }

  println!("Sum {}", total);
}
