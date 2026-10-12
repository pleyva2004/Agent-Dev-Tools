import XCTest
@testable import AgentDevDemo

final class CounterTests: XCTestCase {
    func testIncrementAndReset() {
        var counter = Counter()
        counter.increment()
        counter.increment()
        XCTAssertEqual(counter.value, 2)
        counter.reset()
        XCTAssertEqual(counter.value, 0)
    }
}
