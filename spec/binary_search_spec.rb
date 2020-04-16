require 'binary_search'

my_list = [1, 3, 5, 7, 9]

describe BinarySearch do 
  it 'sorts list, returning position of ' do 
    expect(subject.binary_search(my_list, 3)).to eq 1
  end
end 