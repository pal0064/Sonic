source(here::here("src/r/sum.R"))

test_that("check function my_good_sum", {
  expect_equal(my_good_sum(6, 4), 10)
})
