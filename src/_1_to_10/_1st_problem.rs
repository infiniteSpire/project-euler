pub const TITLE: &str = "Problem nº1: Multiples of 3 or 5";
pub const DESCRIPTION: &str = "Description: If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.";

pub fn solve() {
  let list: Vec<i32> = (1..1000).collect();
  let sum: i32 = list.iter().filter(|&&x| x % 3 == 0 || x % 5 == 0).sum();

  println!("Sum {}", sum);
}
