# frozen_string_literal: true

class SearchAlgorithms
  # sort an ordered list by cutting it in half repeatedly
  def binary_search(list, item)
    # keep track of where you are in list
    low = 0
    high = list.length - 1

    while low <= high
      mid = (low + high) / 2
      guess = list[mid]

      if guess == item
        return mid
      elsif guess > item
        high = mid - 1 # guess too high, get rid of top half of list
      else
        low = mid + 1 # guess too low, get rid bottom half
      end
    end
  end

  def find_smallest(arr)
    smallest = arr[0]
    smallest_index = 0

    arr.each do |int|
      if int < smallest
        smallest = int
        smallest_index = arr.index(int)
      end
    end
    return smallest_index
  end
end