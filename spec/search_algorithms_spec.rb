# frozen_string_literal: true

require 'search_algorithms'

my_list = [1, 3, 5, 7, 9]
even_list = [1, 3, 5, 7]
unordered_list = [3, 4, 2, 1, 4, 7]

describe SearchAlgorithms do
  describe '#binary_search' do
    it 'sorts list, returning position of item' do
      expect(subject.binary_search(my_list, 3)).to eq 1
    end
    it 'sorts list, returning position of item in even list' do
      expect(subject.binary_search(even_list, 3)).to eq 1
    end
    it 'sorts list, returning nil if item not in list ' do
      expect(subject.binary_search(my_list, -3)).to eq nil
    end
  end

  describe '#find_smallest' do
    it 'should return index of lowest int' do
      expect(subject.find_smallest(unordered_list)).to eq 3
    end
  end
end