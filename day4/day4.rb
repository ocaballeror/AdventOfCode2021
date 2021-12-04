# frozen_string_literal: true

require 'set'

def read_input
  numbers = []
  boards = []

  File.open('input') do |file|
    numbers = file.readline.strip.split(',').map(&:to_i)
    file.readline  # empty

    current = {}
    row = 0
    file.each_line do |line|
      line.strip!

      if line.empty?
        boards << current
        current = {}
        row = 0
        next
      end

      current.merge! Hash[line.split.each_with_index.map { |num, col| [num.to_i, [row, col]] }]
      row += 1
    end

    boards << current if current
  end

  [numbers, boards]
end

def dimensions(board)
  lines = Set.new
  rows = Set.new
  board.each_value do |a, b|
    lines << a
    rows << b
  end

  [lines.max, rows.max]
end

def wins?(board, dims)
  lines = Set.new
  rows = Set.new
  board.each_value do |a, b|
    lines << a
    rows << b
  end

  width, height = dims
  lines.size <= width || rows.size <= height
end

def score(board, last)
  board.keys.sum * last
end

def part1
  numbers, boards = read_input
  dims = dimensions(boards[0])

  numbers.each do |num|
    boards.each do |board|
      board.delete num
      return score(board, num) if wins?(board, dims)
    end
  end
end

def part2
  numbers, boards = read_input
  dims = dimensions(boards[0])

  winners = Set.new

  numbers.each do |num|
    boards.each_with_index do |board, idx|
      next if winners.include? idx

      board.delete num
      next unless wins?(board, dims)

      winners << idx
      return score(board, num) if winners.size == boards.size
    end
  end
end

if __FILE__ == $PROGRAM_NAME
  puts "Part 1: #{part1}"
  puts "Part 2: #{part2}"
end
