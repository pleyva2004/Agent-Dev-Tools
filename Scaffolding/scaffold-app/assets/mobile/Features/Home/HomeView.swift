import SwiftUI

struct HomeView: View {
    @State private var model = HomeModel()

    var body: some View {
        NavigationStack {
            VStack(spacing: 20) {
                Text("Count: \(model.counter.value)")
                    .font(.largeTitle)
                    .accessibilityIdentifier("counter")
                Button("Increment", action: model.increment)
                    .buttonStyle(.borderedProminent)
                Button("Reset", action: model.reset)
            }
            .padding()
            .navigationTitle("__APP_NAME__")
        }
    }
}

#Preview { HomeView() }
