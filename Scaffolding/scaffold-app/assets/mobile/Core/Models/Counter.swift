struct Counter {
    private(set) var value = 0

    mutating func increment() { value += 1 }
    mutating func reset() { value = 0 }
}
