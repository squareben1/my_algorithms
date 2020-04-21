# frozen_string_literal: true

require 'binary_search'

my_list = [1, 3, 5, 7, 9]
even_list = [1, 3, 5, 7]

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
end