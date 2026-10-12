import Observation

@MainActor
@Observable
final class HomeModel {
    private(set) var counter = Counter()

    func increment() { counter.increment() }
    func reset() { counter.reset() }
}
