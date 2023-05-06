Feature: Test product listings at Amazon
Scenario: blenders for sale include Google
    Given that we have gone to wwww.amazon.com
     When we search for "smartphone"
     Then we find items from "Google"
      And we find items from "Xiaomi"

